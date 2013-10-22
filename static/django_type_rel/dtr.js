(function ($) {
    $(function () {
        $('.dtr_select').each(function () {
            var select = $(this)
            var url = select.attr('data-url')
            var token = select.parents('form').find('input[name="csrfmiddlewaretoken"]').val()
            var target = $('#' + select.attr('data-target'))
            var def = select.attr('data-default')
            var def_query = select.attr('data-default-query')
            select.change(function () {
                make_for(this.value, url, target, token)
            })
            $('<option>---</option>').prependTo(select).attr("selected", 'selected')
            target.append('<option>---</option>')
            if (def_query && def) {
                select.find("*[value='" + def_query + "']").attr('selected', 'selected')
                make_for(def_query, url, target, token, def)
            }
        })
        function make_for(val, url, target, token, def) {
            var data = {'for': val, 'csrfmiddlewaretoken': token}
            $.post(url, data, function (result) {
                target.find('option').detach()
                for (var i in result) {
                    var option = $("<option value='" + result[i]['pk'] + "'>" + result[i]['value'] + "</option>")

                    option.appendTo(target)
                    if (def && def == result[i]['pk']) {
                        option.attr('selected', 'selected')
                    }
                }
            }, 'json')
        }
    })

})(django.jQuery)