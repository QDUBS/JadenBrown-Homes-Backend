from core.settings import BASE_DIR
def read_file(file_path):
    try:
        with open(f"{BASE_DIR}/templates/{file_path}", "r") as file:
            print(file.read())
    except Exception as exec:
        print(exec)



