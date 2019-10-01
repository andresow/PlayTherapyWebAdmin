<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col">
                <h3>¿ Estas seguro que deseas eliminar este tipo de diagnostico?</h3>              
                <p>Nombre: {{this.element.name}}</p>          
            </div> 
        </div> 
        <div class="row">
            <div class="col">
                <b-button v-on:click="deleteTypeDiagnostic" variant="danger">Eliminar</b-button>
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
            typeDiagnosticId: this.$route.params.typeDiagnosticId,
            element: {
                name: ''
            }
        }
    },
    methods:{
        getTypeDiagnostic (){
            const path= `${process.env.BASE_URI}typeDiagnostic/${this.typeDiagnosticId}/` 
        
            axios.get(path).then((response)=>{
                this.element.name = response.data.name
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        deleteTypeDiagnostic(){
            const path= `${process.env.BASE_URI}typeDiagnostic/${this.typeDiagnosticId}/` 
            axios.delete(path).then((response)=>{
                swal("Tipo de diagnostico eliminado exitosamente", "", "success")
                location.href = '/typeDiagnostic'               
            })
            .catch((error)=>{
                console.log(error)
                swal("No es posible eliminar el tipo de diagnostico", "", "error")
            })
        }       
    },
    created(){
        this.getTypeDiagnostic()
    }
}
</script>