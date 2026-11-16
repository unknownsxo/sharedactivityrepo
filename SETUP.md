# Setup
## 1. Check tools
Run `git --version`. Windows: `py --version`. macOS/Linux: `python3 --version`.
Use Python 3.10+ and Git supporting `git switch`. Open the project folder in your editor.
No packages are required. Ask the tutor if tools are unavailable.

## 2. Partner A establishes the baseline
From the extracted topic6-starter folder, run `git status` first. If it reports an existing repository, stop and ask the tutor to inspect it. Otherwise initialise the new project:
```text
git init -b main
git config user.name "Your Name"
git config user.email "your-approved-email@example.com"
git add .
git commit -m "Establish Topic 6 baseline"
git tag workshop-start
```
Replace identity examples with your own details. Run both check commands from README.md: seven tests should pass and the lint checker should report zero findings.

## 3. Choose the sharing route
Hosted: create an empty private repository on the approved host. Do not generate a README or licence. Give Partner B collaborator access. Replace REPOSITORY_URL below with its actual clone URL:
```text
git remote add origin REPOSITORY_URL
git push -u origin main
git push origin workshop-start
```
Partner B accepts the invitation, then runs these commands from a parent folder:
```text
git clone REPOSITORY_URL topic6-partner-b
cd topic6-partner-b
git config user.name "Your Name"
git config user.email "your-approved-email@example.com"
```
If origin already exists, inspect `git remote -v`; do not replace it blindly. Use the approved sign-in process.

Local: follow docs/local-fallback.md instead of the hosted steps. Do not run both setup routes on the same repository.

## 4. Both partners check readiness
Run both check commands, then:
```text
git status
git rev-parse HEAD
git tag --list
```
Both should be on main with clean working trees, matching starting commits, tag workshop-start and seven passing tests. Record versions, command outputs and role assignments outside the repository. No prepared work is needed.
