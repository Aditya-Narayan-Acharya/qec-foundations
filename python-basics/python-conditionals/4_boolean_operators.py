# The boolean operator AND here means it's TURE if both condition satishfies.
is_member = True
purchase_total = 120

if is_member and purchase_total >= 100:
    print("Discount applies")
else:
    print("No discount")

# The boolean operator OR here means it's TURE if atleast one condition is true.
has_coupon = False
is_vip = True

if has_coupon or is_vip:
    print("discount applies")
else:
    print("no discount")


# The boolean operator NOT here flips a boolean.
is_locked = False
if not is_locked:
    print("you can open the door")
else:
    print("the door is locked") 