$("document").ready(function(){
     $("#insert").click(function () {
      var ename = $("#ename").val();
      var eloc = $("#eloc").val();
      var esal = $("#esal").val();


      $.ajax({
        url: 'create',
         type: 'POST',
        data: {
          'ename': ename,
          'eloc':eloc,
          'esal':esal,
          'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
        },
        success: function (data) {
          $("h1").text("Record Inserted");
          //alert("record Inserted")
          $("#ename").val('');
          $("#eloc").val('');
          $("#esal").val('');

          display();
        }
      });

    });

    $("#display").click(function(){

            display();

    })


}) //end jquery


//display

function display(){
      $.ajax({
            url:"ajaxdisplay",
            type:"GET",
            success:function(response){
                   //$("body").html(response)
                   let rows='';
                   response.dt.forEach(emp=>{
                        rows+=`
                            <tr>
                            <td>${emp.ename}</td>
                            <td>${emp.eloc}</td>
                            <td>${emp.esal}</td>
                            <td><a class="btn btn-danger" onclick="del(${emp.id})">Delete</a></td>
                            </tr>
                        `;
                   });
                   $("tbody").html(rows);
            }
        })
}



function del(id){

    $.ajax({
        url: `delete?eid=${id}`,
         type: 'GET',

        success: function (data) {
         alert("Record Delerted...")
          display();
        }
      });
}