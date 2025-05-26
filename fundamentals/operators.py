def main():
    item_name = 'banana'
    quantity = 5
    discount_rate = 0.1
    eligible_items = "orange banana carrot"
    item_price = 2
    
    ## Arithmetic Operators ##
    # Calculate the subtotal as item_price * quantity
    subtotal = item_price * quantity
    
    # Print item_name and subtotal
    print(f"Item Name: {item_name}, subtotal: {subtotal}")

    # Initialize discout to 0
    discount = 0

    ## Membership Operators ##
    # Check if item_name is in eligible_items string, used to check if item is eligible for a discount
    if item_name in eligible_items:
        discount = subtotal * discount_rate
    # print discount
    print(f"Discount: {discount}")

    ## Comparison Operators ##
    # Check if discount is applied (discount > 0)
    was_discount_applied = discount > 0
    print(f"was the discount applied: {was_discount_applied}")


    ## Logical Operators ##
    # Check if free shipping should be applied (quantity > 5 And item_name='banana')
    does_free_shipping_apply = quantity >= 5 and item_name == 'banana'
    print(f"Is this item eligible for free shipping: {does_free_shipping_apply}")



if __name__ == '__main__':
    main()    