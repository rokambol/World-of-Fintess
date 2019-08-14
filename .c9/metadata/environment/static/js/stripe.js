{"changed":true,"filter":false,"title":"stripe.js","tooltip":"/static/js/stripe.js","value":"$(function() {\n    $(\"#payment-form\").submit(function() {\n        var form = this;\n        var card = {\n            number: $(\"#id_credit_card_number\").val(),\n            expMonth: $(\"#id_expiry_month\").val(),\n            expYear: $(\"#id_expiry_year\").val(),\n            cvc: $(\"#id_cvv\").val()\n        };\n    \n    Stripe.createToken(card, function(status, response) {\n        if (status === 200) {\n            $(\"#credit-card-errors\").hide();\n            $(\"#id_stripe_id\").val(response.id);\n            console.log(status, response);\n\n            // Prevent the credit card details from being submitted\n            // to our server\n            $(\"#id_credit_card_number\").removeAttr('name');\n            $(\"#id_cvv\").removeAttr('name');\n            $(\"#id_expiry_month\").removeAttr('name');\n            $(\"#id_expiry_year\").removeAttr('name');\n\n            form.submit();\n        } else {\n            $(\"#stripe-error-message\").text(response.error.message);\n            $(\"#credit-card-errors\").show();\n            $(\"#validate_card_btn\").attr(\"disabled\", false);\n        }\n    });\n    return false;\n    });\n});","undoManager":{"mark":1,"position":10,"stack":[[{"start":{"row":13,"column":48},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":14,"column":0},"end":{"row":14,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":42},"action":"insert","lines":["console.log(status, response);"],"id":3}],[{"start":{"row":1,"column":42},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":2,"column":0},"end":{"row":2,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["v"],"id":5},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["a"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["S"],"id":7},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":14},"action":"remove","lines":["St"],"id":8},{"start":{"row":2,"column":12},"end":{"row":2,"column":18},"action":"insert","lines":["Stripe"]}],[{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":[" "],"id":9},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["="]}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":86},"action":"insert","lines":["var stripe = Stripe('pk_test_DbyNTqNvVjI8ss63dUztfq8u002UZkloSH');"],"id":10}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":20},"action":"remove","lines":["var Stripe ="],"id":11}],[{"start":{"row":2,"column":7},"end":{"row":2,"column":74},"action":"remove","lines":[" var stripe = Stripe('pk_test_DbyNTqNvVjI8ss63dUztfq8u002UZkloSH');"],"id":12},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":[" "]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":[" "]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"remove","lines":[" "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"remove","lines":["    "]},{"start":{"row":1,"column":42},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":42},"end":{"row":1,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565785426365}