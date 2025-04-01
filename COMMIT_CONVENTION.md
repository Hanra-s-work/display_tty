# Commit convention

This file will describe the norm used for commits in this repository.

This repository does not use the conventional commit down to the letter.

---

## Commit Message Convention

Each commit message must follow one of the two formats below:

- `lowecase infinitive verb: <concise description>`
- `[uppercase infinitive verb] <concise description>`

Additional details about the commit sections:

- **Prefix**: The commit message should always begin with an action verb in its infinitive form. The verb should describe the type of change being made.
- **Description**: After the verb, provide a brief description of what has been done in that commit. Avoid past tense or gerunds (form of a verb that ends in "-ing" and functions as a noun in a sentence).
- **Body (Optional)**: There are no specific rules for the commit body. You can add details as necessary in subsequent lines.

### Examples

- `add: a new service endpoint for user management`
- `fix: login endpoint handling edge cases`
- `update: documentation with new examples`
- `[REMOVE] redundant code from the user service`
- `[EDIT] UI to match updated mockups`
- `[RENAME] Readme.md -> README.md`

### Common Commit Verbs

| Verb         | Description                                          | Example                                 |
|--------------|------------------------------------------------------|-----------------------------------------|
| **ADD**      | Introduces new functionality, features, or files     | `add: cron jobs to clean expired tokens` |
| **FIX**      | Corrects bugs or issues in the codebase              | `fix: the database connection timeout` |
| **UPDATE**   | Improves or modifies existing functionality          | `update: the login flow for better UX` |
| **REMOVE**   | Deletes or removes code, files, or dependencies      | `remove: outdated npm packages`        |
| **EDIT**     | Adjusts or alters existing code without major change | `edit: the README for better clarity`  |
| **REFACTOR** | Refactors code without changing its behavior         | `refactor: server-side validation logic`|
| **RENAME**   | Renames files or variables                           | `rename: variables to follow naming convention` |
| **MERGE**    | Merges branches or pull requests                     | `merge: branch 'feature-auth' into dev`|

### Additional Notes

- **Prefixes** should always be in uppercase to clearly identify the action if they are encapsulated by `[]`, however, if they are followed not encapsulated by `[]` and followed by a `:` they should be in lowercase.
- Try to keep descriptions concise and to the point. Use the body for further elaboration if needed.
- If the commit is related to workflows or external dependencies, be explicit in the description.

### Examples from this Repository

- `add: Player constructor`
- `fix: redundance on constructor arguments`
- `add: AllyMissile and EnemyMissile constructors`
- `add: calling OnCreate() function on constructors`
- `add: Monster and DroppableMonster constructors, Monster TakeDamage`
- `[FIX] the path to the import of the EntityNode.hpp file`
- `[ADD] a window utility management class`
- `[ADD] a window that can open`
- `[FIX] exception handling issues`
- `[UPDATE] the type of the mainloop function`
