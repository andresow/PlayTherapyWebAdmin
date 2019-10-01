<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col">
                <h3>¿ Estas seguro que deseas eliminar esta entidad medica?</h3>              
                <p>Nombre: {{this.element.name}}</p>
            
            </div> 
        </div> 
        <div class="row">
            <div class="col">
                <b-button v-on:click="deleteEntity" variant="danger">Eliminar</b-button>
            </div>
        </div>        
    </div> 
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'

export default {
    data(){
        return{
            entityId: this.$route.params.entityId,
            element: {
                name: ''
            }
        }
    },
    methods:{
        getEntity (){
            const path= `${process.env.BASE_URI}entity/${this.entityId}/` 
        
            axios.get(path).then((response)=>{
                this.element.name = response.data.name
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        deleteEntity(){
            const path= `${process.env.BASE_URI}entity/${this.entityId}/` 
            axios.delete(path).then((response)=>{
                location.href = '/entitys'
                swal("Entidad medica eliminada exitosamente", "", "success")
            })
            .catch((error)=>{
                console.log(error)
                swal("No es posible eliminar la entidad medica", "", "error")
            })
        }       
    },
    created(){
        this.getEntity()
    }
}
</script>