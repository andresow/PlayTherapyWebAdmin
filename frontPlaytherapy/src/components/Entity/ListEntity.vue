<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h2>Listado de entidades médicas registradas.</h2>
                <b-button size="sm" :to="{name: 'CreateEntity'}" variant="primary">
                    Crear entidad medica.
                </b-button>
                <div class="col-md-12">
                    <b-table striped hover :items="entitys" :fields="fields">

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
                { key : 'action', label:''}
            ],
            entitys: []
        }
    },
    methods: {
        getEntitys(){
            const path = `${process.env.BASE_URI}entity/`
            axios.get(path).then((response) =>{
                this.entitys = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    },
    created(){
        this.getEntitys()
    }
}
</script>