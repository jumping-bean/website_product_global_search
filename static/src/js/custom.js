flectra.define('web_product_global_search', function (require) {
    "use strict";
    $(document).ready(function(){
          $('button.oe_search_button_global').on('click', function (e) {
            var $this = $(this);
            if (!e.isDefaultPrevented() && !$this.is(".disabled")) {
                    event.preventDefault();
                    var search = $('input.search-query');
                    window.location = '/shop?' + search.attr('name') + '=' + encodeURIComponent(search.val());
                }
            });
    })
});
