# Private development workbench

`.workbench/` is an optional, ignored directory for local collaboration between
operators, developers, maintainers and agents. Create it when local working context
is useful. It is not committed, packaged, published or required by runtime/CI.
Each checkout may have its own workbench; source synchronization does not transfer
its private contents.

Use it for task instructions, exploratory notes, diagnostics, screenshots and dated
installation validation. Keep maintained architecture, operating procedures and
reproducible verification guidance in the public documentation and code. Workbench
notes never replace the authoritative WAKE record or establish live runtime truth.
Recheck code, installation identity and current operator intent before acting on old
notes. Do not place provider credentials or another installation's authority there.

## Structure and task lifecycle

- `instructions.md`: installation-local guidance for using the workbench.
- `<NNN>-task.md`: pending task, preserving the operator's instructions.
- `<NNN>-task-artifacts/`: optional screenshots and other supporting files.
- `validation/`: dated evidence of tests and observations in that installation.

Update a task with a timestamp, work completed, verification, limitations and next
steps. Keep blocked or unfinished tasks pending. On completion, rename the task to
`done-<NNN>-task.md` and its associated directory to
`done-<NNN>-task-artifacts/`. Update relative artifact links to the renamed directory
so the completed task remains readable. Preserve the original instructions and
artifacts; do not claim completion from an intended change or workflow launch.

A workbench has no committed history. Retain evidence needed by unfinished work and
write concise continuation notes. Other agents and machines must be able to build,
verify and operate the project without this directory. Durable development guidance
belongs in the maintained repository, rather than being available only in private
notes. See the [maintainer map](development.md) for environment and release boundaries.
