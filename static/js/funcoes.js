function autoComplete(inputSelector) {
    // Obtemos a URL e o seletor do campo hidden dos atributos data-url e data-hidden do input
    var inputElement = $(inputSelector);
    var buscaUrl = inputElement.data('url');
    var hiddenSelector = inputElement.data('hidden');

    $(inputSelector).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: buscaUrl,  // URL obtida do atributo data-url
                dataType: "json",
                data: {
                    q: request.term  // O termo digitado no campo de entrada
                },
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            label: item.nome,  // O que será exibido na lista
                            value: item.nome,  // O valor que será preenchido no campo de entrada
                            id: item.id        // O ID que será preenchido no campo hidden
                        };
                    }));
                }
            });
        },
        select: function(event, ui) {
            $(hiddenSelector).val(ui.item.id);  // Atualiza o campo hidden com o ID selecionado
        }
    });
}


        // Função para carregar a imagem no canvas
        function loadImage(base64Image,target_canvas) {

            var img = new Image();
            img.src = base64Image;
           

            img.onload = function() {
                const canvas = document.getElementById(target_canvas);
                const ctx = canvas.getContext('2d');
                var canvasWidth = canvas.width;
                var canvasHeight = canvas.height;
    
                // Dimensões da imagem original
                var imgWidth = img.width;
                var imgHeight = img.height;

                // Calcula a proporção para redimensionamento
                var scaleWidth = canvasWidth / imgWidth;
                var scaleHeight = canvasHeight / imgHeight;
                var scale = Math.min(scaleWidth, scaleHeight); // Mantém a proporção

                // Novas dimensões da imagem
                var newWidth = imgWidth * scale;
                var newHeight = imgHeight * scale;

                // Calcula a posição para centralizar a imagem no canvas
                var offsetX = (canvasWidth - newWidth) / 2;
                var offsetY = (canvasHeight - newHeight) / 2; 

                // Limpa o canvas e desenha a imagem redimensionada
                ctx.clearRect(0, 0, canvasWidth, canvasHeight);
                ctx.drawImage(img, offsetX, offsetY, newWidth, newHeight);
            };

        }