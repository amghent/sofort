/* configuration of the datatable client-side */

$(document).ready(function () {
    $('#questions_dt').DataTable({
        order: [[2, 'desc']],
    });
});
// do not change the id of the datatable !
