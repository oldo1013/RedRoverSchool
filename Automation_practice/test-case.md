**Authorisation**

TC #1 Correct auth
1. Open url:https://www.saucedemo.com
2. Enter login 'standard_user'
3. Enter password 'secret_sauce'
4. Click 'Login' button
5. Check that https://www.saucedemo.com/inventory.html opened

TC #2 Incorrect auth
1. Open url:https://www.saucedemo.com/
2. Enter login 'user'
3. Enter password 'user'
4. Click 'Login' button
5. Check that Error message appeared and text 
"Epic sadface: Username and password do not match any user in this service" presented

**Basket**

TC #3 Add item from catalog
1. Login to portal with correct data
2. Click "Add to cart" button for any product
3. Open basket
4. Check that product is added

TC #4 Remove item from basket
1. Login to portal with correct data
2. Click "Add to cart" button for any product
3. Open basket
4. Click 'Remove' button in basket
5. Check that basket is empty

TC #5 Add item from product card
1. Login to portal with correct data
2. Click on any product in catalog
3. On opened product page click "Add to basket" button
4. Open basket
5. Check that product is added to basket

TC #6 Remove item from basket via product card
1. Login to portal with correct data
2. Click "Add to cart" button for any product card
3. Click 'Remove' button on product card
4. Check that basket is empty

**Product card**

TC #7 Open product via click on product image
1. Login to portal with correct data
2. Click on image on any product card
3. Check that correct product page is opened

TC #8 Open product via click on product name
1. Login to portal with correct data
2. Click on name on any product card
3. Check that correct product page is opened

**Making Order**

TC #9 Make order with correct data
1. Login to portal with correct data
2. Click "Add to cart" button for any product
3. Open basket
4. Click checkout button
5. Fill firstname, lastname and ZIP with correct data
6. Click Continue button
7. Click Finish button
8. Check "Thank you for your order!" page

**Фильтр**

1. Проверка работоспособности фильтра (A to Z)
2. Проверка работоспособности фильтра (Z to A)
3. Проверка работоспособности фильтра (low to high)
4. Проверка работоспособности фильтра (high to low)

**Бургер меню**

1. Выход из системы
2. Проверка работоспособности кнопки "About" в меню
3. Проверка работоспособности кнопки "Reset App State"