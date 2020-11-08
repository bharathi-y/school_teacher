$(document).ready(function () {
    $("#buy-submit-btn").click(function(e){
        $(".loader").show();
        console.log("not able to show")
        stock = $("#id_stock_name").val();
        unit = $("#id_stock_buy_units").val();
        cost = $("#id_stock_price_per_unit").val();
        fee = $("#id_fee").val();
        curr = $("#id_currency").find(":selected").val();
        $.ajax({
            url : '/stocks/buyCostUnit',
            type: 'GET',
            data : {
              'stock_name':stock,
              'currency': curr,
              'stock_buy_units':unit,
              'stock_price_per_unit':cost,
              'fee':fee
            },
            success : function(data){
                console.log(data)
                $("#CurrentHoldingUnits").text(data["unit"]);
                $("#CurrentHoldingCosts").text(data["cost"]);
                $("#currentHoldId").show()
                $(".loader").hide();
            }
        });
    });
}

}
