<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar entidad medica {{form.name}}.</h2>              
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
                                    <b-button type="submit" variant="success">Actualizar</b-button>
                                    <b-button class="btn-large-space" :to="{ name: 'ListEntity' }">Cancelar</b-button>
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
            entityId: this.$route.params.entityId,
            form: {
                name: ''
            }
        }
    },
    methods: {
        onSubmit(event){
            event.preventDefault()
            const path= `${process.env.BASE_URI}entity/${this.entityId}/` 
        
            axios.put(path, this.form).then((response)=>{
                this.form.name = response.data.name
                swal("Entidad medica actualizada exitosamente.", "", "success")
           })
            .catch((error)=>{
                console.log(error)
            })
        },
        getEntity (){
            const path= `${process.env.BASE_URI}entity/${this.entityId}/` 
        
            axios.get(path).then((response)=>{
                this.form.name = response.data.name
            })
            .catch((error)=>{
                console.log(error)
            })
        }       
    },
    created(){
        this.getEntity()
    }
}
</script>