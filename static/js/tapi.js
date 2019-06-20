function printData()
{
   var divToPrint=document.getElementById("hidden-table-info");
   newWin= window.open("");
   newWin.document.write(divToPrint.outerHTML);
   newWin.print();
   newWin.close();
}

function registrationTable() {
   //gets table
    var table = document.getElementsByName('registration-table')[0];

                for(var i = 1; i < table.rows.length; i++)
                {
                    table.rows[i].onclick = function()
                    {
                         document.getElementById("edit_name").value = this.cells[0].innerHTML;
                         document.getElementById("edit_idno").value = this.cells[2].innerHTML;
                         document.getElementById("edit_phone").value = this.cells[1].innerHTML;
                         document.getElementById("edit_location").value = this.cells[3].innerHTML;
                         document.getElementById("edit_status").value = this.cells[5].innerHTML;
                    };
                }

}

function registrationTableDelete() {
   //gets table
    var table = document.getElementsByName('registration-table')[0];

                for(var i = 1; i < table.rows.length; i++)
                {
                    table.rows[i].onclick = function()
                    {
                         document.getElementById("delete_name").value = this.cells[0].innerHTML;
                         document.getElementById("delete_idno").value = this.cells[2].innerHTML;
                         document.getElementById("delete_phone").value = this.cells[1].innerHTML;

                    };
                }

}

function jobTable() {
   //gets table
    var table = document.getElementsByName('job-table')[0];

                for(var i = 1; i < table.rows.length; i++)
                {
                    table.rows[i].onclick = function()
                    {
                         document.getElementById("edit_idno").value = this.cells[0].innerHTML;
                         document.getElementById("edit_department").value = this.cells[1].innerHTML;
                         document.getElementById("edit_position").value = this.cells[2].innerHTML;
                         document.getElementById("edit_salary").value = this.cells[3].innerHTML;
                         document.getElementById("edit_contract").value = this.cells[4].innerHTML;
                         document.getElementById("edit_end_date").value = this.cells[6].innerHTML;
                    };
                }

}

function familyTable() {
   // alert("Hello");
   //gets table
    var table = document.getElementsByName('family-table')[0];
    // var table = document.getElementById('registration-table');

                for(var i = 1; i < table.rows.length; i++)
                {
                    table.rows[i].onclick = function()
                    {
                         // var cellVal = this.cells[0].innerHTML;
                         // alert(cellVal);
                       //rIndex = this.rowIndex;
                         document.getElementById("edit_idno").value = this.cells[2].innerHTML;
                         document.getElementById("edit_phone").value = this.cells[1].innerHTML;
                         document.getElementById("edit_nxtname").value = this.cells[3].innerHTML;
                         document.getElementById("edit_relationship").value = this.cells[4].innerHTML;
                         document.getElementById("edit_location").value = this.cells[5].innerHTML;
                    };
                }

}



