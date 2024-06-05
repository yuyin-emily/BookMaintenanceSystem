function submitForm() {
    $('form').submit();
}

function clearForm() {
    $('form').find('input[type="text"], select').val('');
}

function deleteBook(bookName, bookId) {
    if (confirm('是否刪除 ' + bookName + '？')) {
        alert('刪除成功');
        setTimeout(1000);
        window.location.href = '/delete/' + bookId;
        
    } else {
        alert('已取消');
    }
}
