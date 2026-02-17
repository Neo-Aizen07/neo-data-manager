class RecordManager():
    def __init__(record_manager):
        from storage import file_load
        record_manager.records=file_load(record_manager,silent=True)
        if not isinstance(record_manager.records, dict):
            record_manager.records = {}
    def name_enter(record_manager):
        from user_entry import name_enter
        name_enter(record_manager)
    def search_func(record_manager):
        from operations import search_func
        search_func(record_manager)
    def file_load(record_manager):
        from storage import file_load
        file_load(record_manager)
    def save_names(record_manager):
        from storage import save_names
        save_names(record_manager)
    def qr_code(record_manager):
        from qr_code import qr_code
        qr_code(record_manager)
    def delete_data(record_manager):
        from operations import delete_data
        delete_data(record_manager)
    def delete_person(record_manager):
        from operations import delete_person
        delete_person(record_manager)
    def qr_code(record_manager):
        from qr_code import qr_code
        qr_code(record_manager)