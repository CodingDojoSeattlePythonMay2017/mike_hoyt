// -*- javascript -*-

$(document).ready( function() {
  // Activate JQueryUI elements
  $('#b_date').datepicker();

  // Initialize JQueryUI form elements
  $('#b_date').data( "changed", false );

  $('#b_date').on(
    "change",
    function(){
      $(this).datepicker( "option", "dateFormat", "yy-mm-dd" );
      $(this).data( "changed", true );
    }
  );
})
