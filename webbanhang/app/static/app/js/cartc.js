var updateBtns = document.getElementsByClassName('update-cart')
for (i = 0; i < updateBtns.length; i ++){
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId, 'action', action)
        console.log('user:', user)
        if (user === "AnonymousUser"){
            console.log('user not logged in')

        } else {
            updateUserOrder(productId,action)

        }
    })
}

function updateUserOrder(productId,action){
    console.log('user logged in success add')
    var url = '/update_item/'
    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type':'application/json', 
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) =>{
    return response.json()
    }) 
    .then((data) =>{
        console.log('data', data)
        location.reload()
    }) 
}
// Đoạn mã JavaScript có thể sử dụng jQuery
$('.category-link').click(function(e) {
    e.preventDefault(); // Ngăn chặn hành động mặc định của liên kết
    var categorySlug = $(this).data('category-slug'); // Lấy slug của danh mục từ thuộc tính data
    window.location.href = '/category/?category=' + categorySlug; // Chuyển hướng người dùng đến trang danh mục với tham số category_slug
});

