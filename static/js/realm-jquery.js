$(document).ready(function() {
    var limit = 3;
    $('input.favourite_category_checkbox').on('change', function() {
        if($(this).siblings(':checked').length >= limit) {
            this.checked = false;
        }
    });
});