$(document).ready(function() {
    var max_fields      = 10;
    var wrapper         = $(".input_fields_wrap"); //Fields wrapper
    var add_button      = $(".add_field_button"); //Add button ID
    
    var x = 1;
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="file" id="pic_file" name="pic_file" accept=".png , .jpg"><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }else{
            $("#add_alert").text("เพิ่มรูปได้สูงสุดครั้งละ 10 รูปเท่านั้น!");
        }
    });
    
    $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});
