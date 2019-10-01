<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h2>Crear tipo de diagnostico {{form.name}}.</h2>              
            </div> 
        </div>       
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">
                            <div class="form-group row">
                                <label for="name" class="col-sm-2 col-from-label">Nombre</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Nombre" name="name" class="form-control" v-model.trim="form.name">  
                                </div>                                           
                            </div>
                             <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="success">Crear</b-button>
                                    <b-button class="btn-large-space" :to="{ name: 'ListTypeDiagnostic' }">Cancelar</b-button>
                                </div>
                        </div>
                        </form>                      
                    </div>
                </div>
            </div>
        </div>
    </div>   
</template>

<script>

import axios from 'axios';
import swal from 'sweetalert'

export default {
    data(){
        return {
            form: {
                name: ''
            }
        }
    },
    methods: {
        onSubmit(event){
            event.preventDefault()
            const path= `${process.env.BASE_URI}typeDiagnostic/` 
        
            axios.post(path, this.form).then((response)=>{
                this.form.name = response.data.name
                swal("Tipo de diagnostico creado exitosamente.", "", "success")
           })
            .catch((error)=>{
                swal("No se puede crear el tipo de diagnostico", "", "error")
            })
        },              
    },
    created(){
    }
}

</script>