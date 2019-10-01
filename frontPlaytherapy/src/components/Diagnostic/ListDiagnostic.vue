<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h2>Listado de diagnosticos registrados.</h2>
                <b-button size="sm" :to="{name: 'CreateDiagnostic'}" variant="primary">
                    Crear diagnostico medica.
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
            entityId: this.$route.params.entityId,
            fields: [
                { key : 'name', label:'Nombre'},
                { key : 'code', label:'Codigo'},
                { key : 'type_diagnostic', label:'Tipo de diagnostico'},
                { key : 'action', label:''}
            ],
            typeDiagnostic: []
        }
    },
    methods: {
        getTypeDiagnostic(){
            const path = `${process.env.BASE_URI}diagnostic/`
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