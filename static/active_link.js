$(document).ready(function() {
   var links = $('a.link').click(function() {
       links.removeClass('current');
       $(this).addClass('current');
   });
});
