import streamlit as st
import pandas as pd
from config.database import init_db
from models.inventory import get_all_items, add_item, update_item, delete_item
from services.description_generator import generate_description

# Initialize the database
init_db()

def main():
    st.title("Inventory Management System")

    # Add new item form
    st.header("Add New Item")
    with st.form("add_item_form"):
        new_item_name = st.text_input("Item Name")
        new_category = st.text_input("Category")
        new_quantity = st.number_input("Quantity", min_value=0, step=1)
        new_price = st.number_input("Price", min_value=0.0, step=0.01, format="%.2f")
        submit_button = st.form_submit_button("Add Item")

        if submit_button:
            description = generate_description(new_item_name, new_category, new_quantity)
            add_item(new_item_name, new_category, new_quantity, new_price, description)
            st.success("Item added successfully!")

    # Display inventory
    st.header("Current Inventory")
    items = get_all_items()
    df = pd.DataFrame(items, columns=['ID', 'Item Name', 'Category', 'Quantity', 'Price', 'Description'])
    st.dataframe(df)

    # Update and delete items
    st.header("Update or Delete Item")
    item_to_modify = st.selectbox("Select an item to modify", df['Item Name'].tolist())
    item_id = df[df['Item Name'] == item_to_modify]['ID'].values[0]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Update Item")
        with st.form("update_item_form"):
            update_item_name = st.text_input("Item Name", value=item_to_modify)
            update_category = st.text_input("Category", value=df[df['Item Name'] == item_to_modify]['Category'].values[0])
            update_quantity = st.number_input("Quantity", value=int(df[df['Item Name'] == item_to_modify]['Quantity'].values[0]), min_value=0, step=1)
            update_price = st.number_input("Price", value=float(df[df['Item Name'] == item_to_modify]['Price'].values[0]), min_value=0.0, step=0.01, format="%.2f")
            update_button = st.form_submit_button("Update Item")

            if update_button:
                update_item(item_id, update_item_name, update_category, update_quantity, update_price)
                st.success("Item updated successfully!")

    with col2:
        st.subheader("Delete Item")
        if st.button("Delete Selected Item"):
            delete_item(item_id)
            st.success("Item deleted successfully!")

if __name__ == "__main__":
    main()
