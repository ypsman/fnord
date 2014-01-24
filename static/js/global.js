/*
 * global javascript
 *
 */
(function($) {
	$(document).ready(function() {
		/*
		 * sidebar resize
		 */
		var siteHeight = $(window).height();
		$('#sidebar').height(siteHeight);


		$(window).resize(function() {
			var siteHeight = $(window).height();
			$('#sidebar').height(siteHeight);
		});

		/*
		 * user box
		 */
		$('.box-user').hover(function() {
			$('.btn', this).addClass('active');
			$('.cont', this).show();
		}, function() {
			$('.btn', this).removeClass('active');
			$('.cont', this).hide();
		});

		/*
		 * tabs
		 */
		$('a.link-list').click(function() {
			$(this).parent().next().find('.edit').hide();
			$(this).parent().next().find('.list-view').show();
			$(this).addClass('active');
			$(this).parent().find('.link-edit').removeClass('active');
		});
		$('a.link-edit').click(function() {
			$(this).parent().next().find('.list-view').hide();
			$(this).parent().next().find('.edit').show();
			$(this).addClass('active');
			$(this).parent().find('.link-list').removeClass('active');
		});

        /*
         * buttons copy text and password toggle text
         */
        $('.btn-password-toggle').click(function() {
            var inputType = $(this).prev().attr('type');
            if(inputType == 'password') {
                $(this).prev().attr('type','text');
            } else {
                $(this).prev().attr('type','password');
            }
        });

        $('.text-copy').click(function() {
            var password = $(this).prev().prev().val();
            window.prompt('strg + c / cmd + c for copy!', password);
        });



	});
})(jQuery);