# 1. THAY ĐỔI CẤU TRÚC DỮ LIỆU (Yêu cầu 2)
# Danh sách công việc hiện là danh sách các Dictionary, mỗi Dictionary có 'name' và 'completed'
tasks = [
    {'name': 'Học bài Git và GitHub', 'completed': False},
    {'name': 'Làm bài tập thực hành ở nhà', 'completed': False}
]
def add_task(task_name):
    """Thêm một công việc mới vào danh sách dưới dạng dictionary."""
    # Sửa: Thêm task_name dưới dạng dictionary
    new_task = {'name': task_name, 'completed': False}
    tasks.append(new_task)
    print(f"Đã thêm công việc: '{task_name}'")
def list_tasks():
    """Liệt kê tất cả công việc hiện có, hiển thị trạng thái hoàn thành."""
    if not tasks:
        print("Không có công việc nào trong danh sách.")
        return

    print("\n--- Danh sách công việc ---")
    for index, task in enumerate(tasks, 1):
        # Sửa: Lấy trạng thái completed để hiển thị [x] hoặc [ ]
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")
def complete_task(task_index):
    """Đánh dấu một công việc là hoàn thành dựa trên chỉ số (bắt đầu từ 1)."""
    # Chỉ số người dùng nhập (task_index) phải trừ đi 1 để lấy chỉ số trong list (list_index)
    list_index = task_index - 1
    
    try:
        if 0 <= list_index < len(tasks):
            task = tasks[list_index]
            task['completed'] = True
            print(f"Đã đánh dấu công việc '{task['name']}' là hoàn thành.")
        else:
             print(f"Lỗi: Chỉ số công việc {task_index} không hợp lệ.")
    except IndexError:
        if __name__ == "__main__":
    print(f"Chào mừng đến với ứng dụng To-Do List")
    
    # 1. Liệt kê lần đầu (chưa xong)
    print("\n--- TEST: Trước khi hoàn thành ---")
    list_tasks()

    # 2. Hoàn thành công việc thứ nhất
    complete_task(1) 

    # 3. Liệt kê lần hai (để kiểm tra)
    print("\n--- TEST: Sau khi hoàn thành ---")
    list_tasks()
    # 4. Thêm công việc mới (kiểm tra add_task mới)
    add_task("Kiểm tra lại cấu trúc dictionary")
    list_tasks()

    