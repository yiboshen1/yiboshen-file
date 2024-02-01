from playwright.sync_api import Page


class ProjectListPage:
    """项目列表页"""

    def __init__(self, page: Page):
        self.page = page
        self.locator_add_project = page.get_by_role("button", name="新增项目")
        self.locator_search_project = page.get_by_placeholder("项目名称")
        self.locator_search_button = page.get_by_text('搜索')
        # 新增项目  模态框
        self.locator_add_modal = page.locator('#addModal')
        self.locator_modal_project_name = self.locator_add_modal.get_by_label("项目名称:")
        self.locator_modal_app = self.locator_add_modal.get_by_label("所属应用:")
        self.locator_modal_desc = self.locator_add_modal.get_by_label("项目描述:")
        self.locator_modal_save = self.locator_add_modal.get_by_text('保存')
        self.locator_modal_dismiss = self.locator_add_modal.get_by_text("取消")
        # 编辑项目 模态框
        self.locator_edit_modal = page.locator('#myModal')

        # 刷新按钮
        self.locator_refresh = page.get_by_title('刷新')
        # table 表格按钮
        self.locator_table_tr = page.locator('//tbody/tr')
        self.locator_table_edit = self.locator_table_tr.get_by_title('编辑')
        self.locator_table_delete = self.locator_table_tr.get_by_title('删除')
        self.locator_link_debugtalk = self.locator_table_tr.get_by_text('debugtalk.py')
        # boot-box
        self.locator_boot_box = page.locator('.bootbox-body')
        self.locator_boot_box_accept = page.get_by_text("确定删除")
        self.locator_boot_box_dismiss = page.get_by_text("取消操作")

    def navigate(self):
        self.page.goto("/list_project.html")

    def click_add_project(self):
        self.locator_add_project.click()

    def search_project(self, name):
        self.locator_search_project.fill(name)

    def click_search_button(self):
        self.locator_search_button.click()

    def click_refresh(self):
        self.locator_refresh.click()

