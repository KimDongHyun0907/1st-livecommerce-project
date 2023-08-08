function doSomething(event) {
    event.preventDefault();
}
function submit_func(button){
    var table = document.getElementById('product_table');
    var rowlist = table.rows;
    console.log(document.getElementById('count1').value);
    console.log(document.getElementById('count2').value);
    console.log(document.getElementById('count3').value);
    document.getElementById("data1").value=rowlist[1].innerText+document.getElementById('count1').value;
    document.getElementById("data2").value=rowlist[2].innerText+document.getElementById('count2').value;
    document.getElementById("data3").value=rowlist[3].innerText+document.getElementById('count3').value;

    document.getElementById("hiddenform").submit();
}
function count_price(type, id_name, id_name2){
    const price = document.getElementById(id_name2);
    const price_one = document.getElementById(id_name);
    const sum_price = document.getElementById('sum_price');
    const sum_price_and_shipping = document.getElementById('sum_price_and_shipping');
    var number_text = price.innerText;
    let number = parseInt(number_text.substr(1));

    var number2_text = price_one.innerText;
    let number2 = parseInt(number2_text.substr(1));

    var sum_price_text=sum_price.innerText;
    let sum_number = parseInt(sum_price_text.substr(1));

    var sum_price_and_shipping_text=sum_price_and_shipping.innerText;
    let sum_and_ship_number = parseInt(sum_price_and_shipping_text.substr(1));
    
    if(type === 'plus'){
        number = number + number2;
        sum_number = sum_number + number2;
        sum_and_ship_number = sum_number+2000;
    }
    else if (type === 'minus'){
        if (number === 0){
            type.preventDefault();
        }
        number = number - number2;
        sum_number = sum_number - number2;
        sum_and_ship_number = sum_number+2000;
    }

    price.innerText = '￦'+number.toString();
    sum_price.innerText = '￦'+sum_number.toString();
    sum_price_and_shipping.innerText = '￦'+sum_and_ship_number.toString();

}    
