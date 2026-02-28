# Emulator Validation Matrix

Check each component in sequence:

1. Auth emulator starts
2. Firestore emulator starts
3. Storage emulator starts
4. Functions emulator compiles and starts
5. Expo app can call local endpoints

For each check record:

- command used
- pass/fail
- first actionable error if fail
