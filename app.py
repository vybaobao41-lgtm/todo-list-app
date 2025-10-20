task = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task.append(task_name)
    print(f"Đã thêm công việc:'{task_name}'")
    #--- Điểm bắt đầu của chương trình ---
    def list_tasks():
    """Liệt kê tất cả công việc hiện có trong danh sách."""
    if not tasks:
        print("Không có công việc nào trong danh sách.")
        return

    print("\n--- Danh sách công việc ---")
    # Duyệt qua danh sách và in ra với chỉ số bắt đầu từ 1
    for index, task_name in enumerate(tasks, 1):
        print(f"{index}. {task_name}")
if __name__=="__main":
    print(f"Chào mừng đến với ứng dụng To-Do List")
    add_task("Học bài Git và GitHUb")
    add_task("Làm bài tập thực hành ở nhà")
    