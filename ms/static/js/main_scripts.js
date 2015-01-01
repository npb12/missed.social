$(document).ready(function() {
  $(".datepicker").datepicker()
  $(".menu").menu({
    items: "> :not(.ui-widget-header)"
  });
});
