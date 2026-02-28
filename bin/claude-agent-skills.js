#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');

const PACKAGE_ROOT = path.resolve(__dirname, '..');
const DEFAULT_SOURCE = path.join(PACKAGE_ROOT, 'skills');

function readPackageVersion() {
  const pkgPath = path.join(PACKAGE_ROOT, 'package.json');
  try {
    const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
    return pkg.version || '0.0.0';
  } catch {
    return '0.0.0';
  }
}

function printHelp() {
  console.log(`claude-agent-skills v${readPackageVersion()}\n`);
  console.log('Usage:');
  console.log('  claude-agent-skills list [--source <path>] [--json]');
  console.log('  claude-agent-skills install <skill-name> [--source <path>] [--target <path>] [--force] [--dry-run]');
  console.log('  claude-agent-skills install --all [--source <path>] [--target <path>] [--force] [--dry-run]');
  console.log('  claude-agent-skills uninstall <skill-name> [--target <path>] [--dry-run]');
  console.log('  claude-agent-skills uninstall --all [--source <path>] [--target <path>] [--dry-run]');
  console.log('  claude-agent-skills help');
  console.log('');
  console.log('Defaults:');
  console.log('  source: this package\'s skills/ directory');
  console.log('  target: $CLAUDE_HOME/skills or $CODEX_HOME/skills or ~/.claude/skills');
}

function fail(message) {
  console.error(`Error: ${message}`);
  process.exit(1);
}

function expandHome(inputPath) {
  if (!inputPath) return inputPath;
  if (inputPath === '~') return os.homedir();
  if (inputPath.startsWith('~/')) return path.join(os.homedir(), inputPath.slice(2));
  return inputPath;
}

function resolveSource(sourceArg) {
  const source = path.resolve(expandHome(sourceArg || DEFAULT_SOURCE));
  if (!fs.existsSync(source) || !fs.statSync(source).isDirectory()) {
    fail(`source directory not found: ${source}`);
  }
  return source;
}

function resolveTarget(targetArg) {
  if (targetArg) {
    return path.resolve(expandHome(targetArg));
  }

  const claudeHome = process.env.CLAUDE_HOME;
  if (claudeHome && claudeHome.trim()) {
    return path.join(claudeHome, 'skills');
  }

  const codexHome = process.env.CODEX_HOME;
  if (codexHome && codexHome.trim()) {
    return path.join(codexHome, 'skills');
  }

  return path.join(os.homedir(), '.claude', 'skills');
}

function isSkillDir(dirPath) {
  const skillFile = path.join(dirPath, 'SKILL.md');
  return fs.existsSync(skillFile) && fs.statSync(skillFile).isFile();
}

function listSkillNames(sourceDir) {
  const entries = fs.readdirSync(sourceDir, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .filter((name) => isSkillDir(path.join(sourceDir, name)))
    .sort((a, b) => a.localeCompare(b));
}

function parseFrontmatter(skillMdContent) {
  if (!skillMdContent.startsWith('---\n')) return null;
  const endIndex = skillMdContent.indexOf('\n---\n', 4);
  if (endIndex === -1) return null;
  return skillMdContent.slice(4, endIndex);
}

function validateSkillDir(skillDir) {
  const skillFile = path.join(skillDir, 'SKILL.md');
  if (!fs.existsSync(skillFile)) {
    throw new Error(`missing SKILL.md in ${skillDir}`);
  }

  const content = fs.readFileSync(skillFile, 'utf8');
  const frontmatter = parseFrontmatter(content);
  if (!frontmatter) {
    throw new Error(`invalid frontmatter in ${skillFile}`);
  }

  if (!/^name:\s*.+$/m.test(frontmatter)) {
    throw new Error(`missing frontmatter name in ${skillFile}`);
  }
  if (!/^description:\s*.+$/m.test(frontmatter)) {
    throw new Error(`missing frontmatter description in ${skillFile}`);
  }
}

function copySkill(srcDir, dstDir, force, dryRun) {
  const alreadyExists = fs.existsSync(dstDir);
  if (alreadyExists) {
    if (!force) return 'skipped';
    if (!dryRun) fs.rmSync(dstDir, { recursive: true, force: true });
  }

  if (!dryRun) {
    fs.cpSync(srcDir, dstDir, { recursive: true });
    validateSkillDir(dstDir);
  }

  return alreadyExists && force ? 'replaced' : 'installed';
}

function removeSkill(dstDir, dryRun) {
  if (!fs.existsSync(dstDir)) {
    return 'absent';
  }
  if (!dryRun) {
    fs.rmSync(dstDir, { recursive: true, force: true });
  }
  return 'removed';
}

function parseOptions(args) {
  const opts = {
    all: false,
    force: false,
    dryRun: false,
    json: false,
    source: null,
    target: null,
    positional: []
  };

  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];
    if (arg === '--all') {
      opts.all = true;
      continue;
    }
    if (arg === '--force') {
      opts.force = true;
      continue;
    }
    if (arg === '--dry-run') {
      opts.dryRun = true;
      continue;
    }
    if (arg === '--json') {
      opts.json = true;
      continue;
    }
    if (arg === '--source') {
      if (i + 1 >= args.length) fail('missing value for --source');
      opts.source = args[i + 1];
      i += 1;
      continue;
    }
    if (arg === '--target') {
      if (i + 1 >= args.length) fail('missing value for --target');
      opts.target = args[i + 1];
      i += 1;
      continue;
    }
    if (arg.startsWith('--')) {
      fail(`unknown option: ${arg}`);
    }
    opts.positional.push(arg);
  }

  return opts;
}

function commandList(opts) {
  const sourceDir = resolveSource(opts.source);
  const names = listSkillNames(sourceDir);

  if (opts.json) {
    console.log(JSON.stringify({ source: sourceDir, count: names.length, skills: names }, null, 2));
    return;
  }

  console.log(`Source: ${sourceDir}`);
  for (const name of names) {
    console.log(`- ${name}`);
  }
  console.log(`Total: ${names.length}`);
}

function commandInstall(opts) {
  const sourceDir = resolveSource(opts.source);
  const targetDir = resolveTarget(opts.target);
  const names = listSkillNames(sourceDir);

  const selected = opts.all ? names : [opts.positional[0]].filter(Boolean);
  if (!selected.length) {
    fail('provide a skill name or use --all');
  }

  const available = new Set(names);
  for (const name of selected) {
    if (!available.has(name)) {
      fail(`skill not found in source: ${name}`);
    }
  }

  if (!opts.dryRun) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const results = [];
  for (const name of selected) {
    const src = path.join(sourceDir, name);
    const dst = path.join(targetDir, name);
    const status = copySkill(src, dst, opts.force, opts.dryRun);
    results.push({ skill: name, status });
  }

  console.log(`Target: ${targetDir}`);
  for (const result of results) {
    console.log(`- ${result.skill}: ${result.status}${opts.dryRun ? ' (dry-run)' : ''}`);
  }
}

function commandUninstall(opts) {
  const sourceDir = resolveSource(opts.source);
  const targetDir = resolveTarget(opts.target);
  const names = listSkillNames(sourceDir);

  const selected = opts.all ? names : [opts.positional[0]].filter(Boolean);
  if (!selected.length) {
    fail('provide a skill name or use --all');
  }

  const results = [];
  for (const name of selected) {
    const dst = path.join(targetDir, name);
    const status = removeSkill(dst, opts.dryRun);
    results.push({ skill: name, status });
  }

  console.log(`Target: ${targetDir}`);
  for (const result of results) {
    console.log(`- ${result.skill}: ${result.status}${opts.dryRun ? ' (dry-run)' : ''}`);
  }
}

function main() {
  const argv = process.argv.slice(2);
  const command = argv[0];

  if (!command || command === 'help' || command === '--help' || command === '-h') {
    printHelp();
    return;
  }

  const opts = parseOptions(argv.slice(1));

  if (command === 'list') {
    commandList(opts);
    return;
  }

  if (command === 'install') {
    commandInstall(opts);
    return;
  }

  if (command === 'uninstall') {
    commandUninstall(opts);
    return;
  }

  fail(`unknown command: ${command}`);
}

main();
