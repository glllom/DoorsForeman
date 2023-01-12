function table_filter(keyword) {
    let rows = document.getElementsByClassName('tr');
    Array.prototype.slice.call(rows, 0).forEach((item, index) => {
        item.hidden = item.outerText.match(keyword) == null;
    });
}


function add_door(options) {
    const tbody = document.getElementById('doors_table_id');
    const last_row = tbody.lastElementChild
    let new_row = last_row.cloneNode(true);
    new_row.children[1].firstElementChild.value = last_row.children[1].firstElementChild.value
    new_row.children[5].firstElementChild.value = last_row.children[5].firstElementChild.value
    new_row.firstElementChild.innerText = parseInt(new_row.firstElementChild.innerText) + 1;
    for (let child of new_row.children) {
        if (child.children.length > 0) {
            child.firstElementChild.id = child.firstElementChild.id.slice(0, -1) +
                (parseInt(child.firstElementChild.id.slice(-1)) + 1);
        }
    }
    if (options['lock']){
        console.log(`found lock ${options['lock']}`)
    }
    tbody.appendChild(new_row);
    return new_row.firstElementChild.innerText
}

function add_new_group_doors() {
  let lock = document.getElementById("id_lock").value;
  let hinges = document.getElementById("id_hinges").value;
  let door_type = document.getElementById("id_door_type").value;
  let engraving = document.getElementById("id_engraving").value;
  console.log(lock, hinges, door_type, engraving );
  add_door({ 'lock': lock, 'hinges': hinges, 'door_type': door_type, 'engraving': engraving });
}

function test() {
    console.log("test");
}

function call_print() {
    window.onafterprint = window.close;
    window.print();
}


let filter_keyword = document.getElementsByClassName('filter')[0];
if (filter_keyword) {
    filter_keyword.addEventListener('keyup', () => {
        table_filter(filter_keyword.value);
    });
}

let copy_door_btn = document.getElementById('copy_door_btn');
let new_doors_group_btn = document.getElementById('new_doors_group_btn');
let print_btn = document.getElementById("print_btn");
let image_filename = document.getElementById("id_image")

if (print_btn) {
    print_btn.addEventListener('click', call_print);
}

if (image_filename)
    image_filename.addEventListener('mouseout', () => {
        const [file] = image_filename.files;
        if (file) {
            document.getElementById("preview").src = URL.createObjectURL(file);
        }
    });
