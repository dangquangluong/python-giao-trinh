"""
Chuong 9: Du an CLI Todo App

Su dung:
    python todo_cli.py add "Hoc Python"
    python todo_cli.py list
    python todo_cli.py done 1
    python todo_cli.py delete 1
"""

import json
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional


# === Model ===
@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    completed_at: Optional[str] = None


# === Storage ===
DATA_FILE = Path("todo_data.json")


def load_tasks() -> List[Task]:
    """Doc danh sach task tu file."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Task(**item) for item in data]


def save_tasks(tasks: List[Task]):
    """Luu danh sach task vao file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, ensure_ascii=False, indent=2)


def get_next_id(tasks: List[Task]) -> int:
    """Lay ID tiep theo."""
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1


# === Commands ===
def cmd_add(title: str):
    """Them task moi."""
    tasks = load_tasks()
    new_task = Task(id=get_next_id(tasks), title=title)
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Da them: [{new_task.id}] {new_task.title}")


def cmd_list(filter_status: Optional[str] = None):
    """Liet ke cac task."""
    tasks = load_tasks()

    if filter_status == "done":
        tasks = [t for t in tasks if t.done]
    elif filter_status == "pending":
        tasks = [t for t in tasks if not t.done]

    if not tasks:
        print("Khong co task nao.")
        return

    print(f"\n{'ID':<4} {'Trang Thai':<12} {'Tieu De'}")
    print("-" * 50)
    for task in tasks:
        status = "[x]" if task.done else "[ ]"
        print(f"{task.id:<4} {status:<12} {task.title}")
    print(f"\nTong: {len(tasks)} task")


def cmd_done(task_id: int):
    """Danh dau task hoan thanh."""
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.done = True
            task.completed_at = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Da hoan thanh: [{task.id}] {task.title}")
            return
    print(f"Khong tim thay task voi ID={task_id}")


def cmd_delete(task_id: int):
    """Xoa task."""
    tasks = load_tasks()
    original_len = len(tasks)
    tasks = [t for t in tasks if t.id != task_id]

    if len(tasks) == original_len:
        print(f"Khong tim thay task voi ID={task_id}")
        return

    save_tasks(tasks)
    print(f"Da xoa task ID={task_id}")


def cmd_clear():
    """Xoa tat ca task da hoan thanh."""
    tasks = load_tasks()
    remaining = [t for t in tasks if not t.done]
    removed = len(tasks) - len(remaining)
    save_tasks(remaining)
    print(f"Da xoa {removed} task da hoan thanh")


# === Main ===
def print_usage():
    """In huong dan su dung."""
    print("""
Todo CLI - Quan ly cong viec

Su dung:
    python todo_cli.py add <title>       Them task moi
    python todo_cli.py list [filter]     Liet ke task (filter: done/pending)
    python todo_cli.py done <id>         Danh dau hoan thanh
    python todo_cli.py delete <id>       Xoa task
    python todo_cli.py clear             Xoa tat ca task da hoan thanh
    """)


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Loi: Can nhap tieu de task")
            return
        cmd_add(" ".join(sys.argv[2:]))

    elif command == "list":
        filter_status = sys.argv[2] if len(sys.argv) > 2 else None
        cmd_list(filter_status)

    elif command == "done":
        if len(sys.argv) < 3:
            print("Loi: Can nhap ID task")
            return
        cmd_done(int(sys.argv[2]))

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Loi: Can nhap ID task")
            return
        cmd_delete(int(sys.argv[2]))

    elif command == "clear":
        cmd_clear()

    else:
        print(f"Lenh khong hop le: {command}")
        print_usage()


if __name__ == "__main__":
    main()
