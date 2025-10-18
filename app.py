task = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task.append(task_name)
    print(f"Đã thêm công việc:'{task_name}'")
    #--- Điểm bắt đầu của chương trình ---
if __name__=="__main":
    print(f"Chào mừng đến với ứng dụng To-Do List")
    add_task("Học bài Git và GitHUb")
    add_task("Làm bài tập thực hành ở nhà")
    