<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h2>Listado de tipos de diagnosticos registradas.</h2>
                <b-button size="sm" :to="{name: 'CreateTypeDiagnostic'}" variant="primary">
                    Crear tipo de diagnostico.
                </b-button>
                <div class="col-md-12">
                    <b-table striped hover :items="typeDiagnostic" :fields="fields">

                        <template v-slot:cell(action)="row" slote-scope="data">
                            <b-button size="sm" variant="primary" >
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger"  >
                                Eliminar
                            </b-button>
                         </template>

                    </b-table>
                </div>
            </div> 
        </div>
    </div>   
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return{
            typeDiagnosticId: this.$route.params.typeDiagnosticId,
            fields: [
                { key : 'name', label:'Nombre'},
                { key : 'action', label:''}
            ],
            typeDiagnostic: []
        }
    },
    methods: {
        getTypeDiagnostic(){
            const path = `${process.env.BASE_URI}typeDiagnostic/`
            axios.get(path).then((response) =>{
                this.typeDiagnostic = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    },
    created(){
        this.getTypeDiagnostic()
    }
}
</script>