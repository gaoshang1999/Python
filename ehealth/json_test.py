import json

a = "[{'ItemNo': u'85123A', 'UnitPrice': 2.55, 'Description': u'ADORIAN CROSSBOW', 'Quantity': 6}, {'ItemNo': 71053, 'UnitPrice': 3.39, 'Description': u'WHITE METAL LANTERN', 'Quantity': 6}, {'ItemNo': u'84406B', 'UnitPrice': 2.75, 'Description': u'CREAM CUPID HEARTS COAT HANGER', 'Quantity': 8}, {'ItemNo': u'84029G', 'UnitPrice': 3.39, 'Description': u'KNITTED UNION FLAG HOT WATER BOTTLE', 'Quantity': 6}, {'ItemNo': u'84029E', 'UnitPrice': 3.39, 'Description': u'RED WOOLLY HOTTIE WHITE HEART.', 'Quantity': 6}, {'ItemNo': 22752, 'UnitPrice': 7.65, 'Description': u'SET 7 BABUSHKA NESTING BOXES', 'Quantity': 2}, {'ItemNo': 21730, 'UnitPrice': 4.25, 'Description': u'GLASS STAR FROSTED T-LIGHT HOLDER', 'Quantity': 6}]"

b = eval(a)
    
print(type(b[0]))


a = "'Description': u'Dotcomgiftshop Gift Voucher \xa340.00'"

print( a.replace("\\", "\\\\"))