# Contributing to Display TTY

Thank you for considering contributing to Display TTY! This document outlines the guidelines and processes for making contributions to the project.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
    - [Reporting Issues](#reporting-issues)
    - [Feature Requests](#feature-requests)
    - [Submitting Changes](#submitting-changes)
3. [Coding Guidelines](#coding-guidelines)
4. [Commit Message Convention](#commit-message-convention)
5. [Pull Request Process](#pull-request-process)

---

## Code of Conduct

We adhere to a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive environment for all contributors. Please read it before contributing.

---

## How to Contribute

### Reporting Issues

If you encounter a bug or have a question:

1. Check if the issue has already been reported in the [Issues section](https://github.com/Hanra-s-work/display_tty/issues).
2. If not, create a new issue using the **Bug Report** or **Question** template.
3. Include detailed steps to reproduce the bug or context about your question.

### Feature Requests

To propose a new feature:

1. Check if the feature has already been requested.
2. Open a new issue using the **Feature Request** template.
3. Clearly describe the problem the feature solves and, if possible, provide examples of how it would be used.

### Submitting Changes

To contribute code:

1. Fork the repository.
2. Create a new branch following the naming convention: `feature/<description>` or `fix/<description>`
3. Make your changes following the [Coding Guidelines](#coding-guidelines).
4. Test your changes thoroughly.

---

## Coding Guidelines

- Follow the repository’s style guide and adhere to best practices.
- Ensure all code is **well-documented** and includes meaningful comments.
- Write tests where applicable and ensure all existing tests pass.
- Use the following tools (if applicable):
  - **Docker** for containerization.
  - **Github Actions** for CI/CD.

---

## Commit Message Convention

All commit messages **must** follow the format below:
`[INFLECTED VERB] <concise description>`

See [COMMIT_CONVENTION.md](COMMIT_CONVENTION.md) for details and examples.

---

## Pull Request Process

1. Ensure your branch is up to date with the `main` branch.
2. Create a pull request with a clear title and description of your changes.
3. Link any relevant issues in the pull request description.
4. Ensure the following checks pass:
   - Code adheres to the guidelines.
   - All tests pass.
   - There are no conflicts with the `main` branch.

5. A reviewer will assess your pull request. Please address their feedback promptly.
