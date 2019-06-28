// Configure CSRF
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

$(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    });
});

// Save ingredients
$(function () {
    $(".save").click(function () {
        var ingredients = $(event.target).closest(".recipe").find("input.form-control").tokenfield('getTokensList')
        var recipeId = $(event.target).closest(".recipe").find("input.form-control").attr("id")
        $.post("/save_recipe_changes", {
                ingredients: ingredients,
                recipeId: recipeId
            });

    })
});
