# Git Branching Practice: Mini Python Task Manager

A small command-line Python application used to practise Git and GitHub workflows.

## Requirements

- Python 3.10+
- Git
- VS Code (recommended)
- GitHub account (for the remote repository exercises)

## Run the starter application

```powershell
python app.py
```

## Create the repository

Run these commands from this project folder:

```powershell
git init
git add .
git commit -m "chore: add starter task manager"
git branch -M main
git status
git log --oneline
```

## Practice roadmap

### Phase 1 — Baseline
1. Run `python app.py`.
2. Add and list a task.
3. Review `git status`, `git diff`, and `git log --oneline`.

### Phase 2 — Create develop
```powershell
git switch -c develop
git push -u origin develop
```
The push command is used after you create and connect a GitHub repository.

### Phase 3 — Feature branch: add task validation
```powershell
git switch develop
git switch -c feature/add-task-validation
```
Change `add_task()` so an empty task name is rejected. Test it manually, then commit:
```powershell
git diff
git add app.py
git commit -m "feat: validate task names"
git switch develop
git merge --no-ff feature/add-task-validation
```

### Phase 4 — Feature branch: mark tasks complete
```powershell
git switch -c feature/complete-task
```
Add a menu option and a `complete_task()` function. Ask for a task number, validate it, and set its `completed` value to `True`. Test valid and invalid numbers, commit, and merge into `develop`.

### Phase 5 — Feature branch: delete tasks
Create `feature/delete-task` from `develop`. Add a menu option and a `delete_task()` function. Validate the selected task number before removing an item. Commit and merge into `develop`.

### Phase 6 — Bug-fix branch
Create `bugfix/invalid-task-number` from `develop`. Make sure complete/delete operations handle non-numeric input and out-of-range numbers without crashing. Commit and merge.

### Phase 7 — Merge conflict simulation
1. Create `feature/menu-message` from `develop` and change the invalid-choice message in `app.py`.
2. Commit that change.
3. Switch back to `develop`, change the exact same line to a different message, and commit.
4. Merge the feature branch into `develop`. Git should report a conflict.
5. Open `app.py`, find `<<<<<<<`, `=======`, and `>>>>>>>`, choose the final wording, remove all markers, then:
```powershell
git add app.py
git commit -m "fix: resolve menu message conflict"
```

### Phase 8 — Release to main
Run the application and test all features. Then:
```powershell
git switch main
git merge --no-ff develop
git log --oneline --graph --decorate --all
```

### Phase 9 — Remote GitHub practice
Create an empty GitHub repository named `git-python-practice` (do not initialise it with a README if you already have one locally), then connect it:
```powershell
git remote add origin https://github.com/YOUR-USERNAME/git-python-practice.git
git push -u origin main
git push -u origin develop
git push -u origin --all
```
Replace `YOUR-USERNAME` with your GitHub username. If `origin` already exists, inspect it with `git remote -v` before changing it.

Practise remote updates:
```powershell
git fetch origin
git branch -a
git pull
```

## Useful Git commands

```powershell
git status
git branch
git branch -a
git switch BRANCH-NAME
git switch -c NEW-BRANCH
git diff
git diff --staged
git log --oneline --graph --decorate --all
git show
git merge --no-ff BRANCH-NAME
git merge --abort
git stash
git stash pop
```

## Completion checklist

- [ ] Create `main` and `develop`
- [ ] Create at least three feature branches
- [ ] Make separate code changes and commits on each branch
- [ ] Merge features into `develop`
- [ ] Fix a bug in a separate branch
- [ ] Create and resolve a real merge conflict
- [ ] Merge tested work into `main`
- [ ] Push branches to GitHub
- [ ] Inspect branch history using `git log --graph`
- [ ] Explain the difference between `fetch` and `pull`, and `merge` and `rebase`
