from playwright.sync_api import Page


class OrdersHistoryPage:
    """Page Object Model for Orders History Page"""
    
    def __init__(self, page: Page):
        self.page = page
        self.orders_table = page.locator("table")
        self.order_rows = page.locator("tbody tr")
        self.order_id_column = page.locator("th, td")  # Order ID appears in table cells
    
    def is_orders_page_loaded(self) -> bool:
        """Verify that orders history page is loaded"""
        try:
            self.orders_table.wait_for(state='visible', timeout=15000)
            return True
        except:
            return False
    
    def find_order_id_in_table(self, order_id: str) -> bool:
        """Find and verify the order ID exists in the Your Orders table"""
        try:
            # Wait for table to be visible
            self.orders_table.wait_for(state='visible', timeout=15000)
            
            # Get all table rows
            row_count = self.order_rows.count()
            
            # Search through all rows for the order ID
            for i in range(row_count):
                row_text = self.order_rows.nth(i).inner_text()
                # Check if order ID exists in this row (case-insensitive)
                if order_id.lower() in row_text.lower():
                    return True
            
            # Alternative: Search in all table cells
            cells = self.page.locator("td, th")
            cell_count = cells.count()
            for i in range(cell_count):
                cell_text = cells.nth(i).inner_text()
                if order_id.lower() in cell_text.lower():
                    return True
            
            return False
        except Exception as e:
            print(f"Error finding order ID in table: {str(e)}")
            return False
    
    def get_order_count(self) -> int:
        """Get the number of orders in the table"""
        try:
            return self.order_rows.count()
        except:
            return 0

