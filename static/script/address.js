function chamarModalEdit(endereco) {
    var address = JSON.parse(endereco.replace(/'/g, '"'));
    var modal = `
    <div class="modal-dialog">
    <div class="modal-content">
        <div class="modal-header">
            <h5>Edite as informações do endereço</h5>
            <button type="button" class="close" data-dismiss="modal">X</button>

        </div>
        <div class="modal-body">


            <form class="form" method="POST">

                <div class="input-group mb-3">

                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1"><i
                                class="fa-solid fa-id-badge"></i></span>
                    </div>
                    <input type="string" class="form-control" value="${address[0]}"
                        aria-describedby="basic-addon1" name="name" required>

                </div>
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1"><i
                                class="fa-solid fa-location-dot"></i></span>
                    </div>

                    <input type="string" class="form-control"
                        aria-describedby="basic-addon1" name="cep" id="edit_cep" onblur="pesquisacep(this.value, 'edit_');" value="${address[1]}">

                </div>
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1"><i
                                class="fa-solid fa-road"></i></span>
                    </div>

                    <input type="string" class="form-control"
                        aria-describedby="basic-addon1" name="street" id="edit_street" readonly value="${address[2]}">

                </div>
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1"><i
                                class="fa-solid fa-house"></i></span>
                    </div>
                    <input type="string" class="number"
                        aria-describedby="basic-addon1" name="number" value="${address[3]}">

                    <span class="input-group-text" id="basic-addon1"><i
                            class="fa-solid fa-hashtag"></i></span>

                    <input type="string" class="h-15 complement"value="${address[4]}"
                        aria-describedby="basic-addon1" name="complement">

                </div>

                <div class="input-group mb-3">

                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1"><i
                                class="fa-solid fa-house"></i></span>
                    </div>
                    <input type="string" class="form-control" value="${address[5]}"
                        aria-describedby="basic-addon1" name="zone" id="edit_zone" readonly >

                </div>
                <div class="input-group mb-3">

                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1"><i
                                class="fa-solid fa-building"></i></span>
                    </div>
                    <input type="string" class="form-control" value="${address[6]}"
                        aria-describedby="basic-addon1" name="city" id="edit_city" readonly >

                </div>
                <div class="input-group mb-3">

                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1"><i
                                class="fa-solid fa-building"></i></span>
                    </div>
                    <input type="string" class="form-control" value="${address[7]}"
                        aria-describedby="basic-addon1" name="state" id="edit_state" readonly
                        >
                    <input type="hidden" class="form-control" value="${address[8]}"
                        aria-describedby="basic-addon1" name="id" id="edit_id" readonly
                        >

                </div>
                <div class="input-group mb-3">
                            
                    <div class="form-check">
                        <input checked="" class="form-check-input" disabled="" id="set_default" name="set_default" placeholder="Endereço Padrão" required type="checkbox" value="y">
                        <label class="form-check-label">
                        
                            Endereço Padrão
                        </label>
                    </div>

                </div>
                
                <a href="{{url_for('edit_address')}}"></a><button type="submit" class="btn btn-add" name="edit_address">Editar endereço</button>
            </form>
        </div>
    </div>
    <div class="modal-footer">
    </div>
</div>
`;
        document.getElementById('edit_address').innerHTML = modal;
}

function chamarModalExclude(endereco, url) {
    var address = JSON.parse(endereco.replace(/'/g, '"'));
    var modal = `
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">X</button>
                </div>
                <div class="modal-body">
                    <h5>Você quer excluir esse endereço?</h5>
                    <p class="user-address">${address[0]}</p>
                    <hr>
                    <p class="user-name-address">${address[2]}, ${address[3]}</p>
                    <p class="user-name-address">${address[5]}, ${address[6]}, ${address[7]}</p>
                    <p class="user-name-address">CEP:${address[1]}</p>
                    <a href="${url}?id=${address[8]}"><button
                            type="submit" class="btn btn-secondary">Sim</button></a>
                    <button type="button" class="btn btn-secondary" data-toggle="modal"
                        data-target="#exclude_address">Não</button>
                </div>
            </div>
        </div>
`;
        document.getElementById('exclude_address').innerHTML = modal;
}

function limpa_formulário_cep(prefix="") {
        //Limpa valores do formulário de cep.
        document.getElementById(prefix + 'street').value=("");
        document.getElementById(prefix + 'zone').value=("");
        document.getElementById(prefix + 'city').value=("");
        document.getElementById(prefix + 'state').value=("");
        
}

function meu_callback(conteudo, prefix="") {
    console.log(conteudo);
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById(prefix + 'street').value=(conteudo.logradouro);
        document.getElementById(prefix + 'zone').value=(conteudo.bairro);
        document.getElementById(prefix + 'city').value=(conteudo.localidade);
        document.getElementById(prefix + 'state').value=(conteudo.uf);

    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulário_cep(prefix);
        alert("CEP não encontrado.");
    }
}

function meu_callback_edit(conteudo, prefix="edit_") {
    console.log(conteudo);
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById(prefix + 'street').value=(conteudo.logradouro);
        document.getElementById(prefix + 'zone').value=(conteudo.bairro);
        document.getElementById(prefix + 'city').value=(conteudo.localidade);
        document.getElementById(prefix + 'state').value=(conteudo.uf);

    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulário_cep(prefix);
        alert("CEP não encontrado.");
    }
}

function pesquisacep(valor, prefix="") {

    //Nova variável "cep" somente com dígitos.
    var cep = valor.replace(/\D/g, '');

    //Verifica se campo cep possui valor informado.
    if (cep != "") {

        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if(validacep.test(cep)) {

            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById(prefix + 'street').value="...";
            document.getElementById(prefix + 'zone').value="...";
            document.getElementById(prefix + 'city').value="...";
            document.getElementById(prefix + 'state').value="...";
            //Cria um elemento javascript.
            var script = document.createElement('script');

            //Sincroniza com o callback.
            if (prefix.search('edit') > -1) {
                script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback_edit';
            }
            else {
                script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';
            }

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

        } //end if.
        else {
            //cep é inválido.
            limpa_formulário_cep(prefix);
            alert("Formato de CEP inválido.");
        }
    } //end if.
    else {
        //cep sem valor, limpa formulário.
        limpa_formulário_cep(prefix);
    
    }
};



