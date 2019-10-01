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
                            <div class="form-group row">
                                <label for="name" class="col-sm-2 col-from-label">Codigo</label>
                                
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Codigo" name="code" class="form-control" v-model.trim="form.code">  
                                </div>                                                                      
                            </div>
                            <div class="form-group row">
                                <label for="typeDiagnostic" class="col-sm-2 col-from-label">Tipo de diagnostico</label>        
                                <div class="col-sm-6">

                                    <b-form-select typeDiagnostic class="mb-3" v-model.trim="form.type_diagnostic">
                                    <template v-slot:first>
                                        <option :value="null" disabled>-- Porfavor selecione un tipo de diagnostico --</option>
                                    </template>
                                        <option v-for="typeDiagnostic in typeDiagnostic" :key="typeDiagnostic.id" :value="typeDiagnostic.id" >{{ typeDiagnostic.name }} </option>
                                    </b-form-select>
                                      
                                </div>                                                                      
                            </div>   
                             <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="success">Actualizar</b-button>
                                    <b-button class="btn-large-space" :to="{ name: 'ListDiagnostic' }">Cancelar</b-button>
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
            diagnosticId: this.$route.params.diagnosticId,
            form: {
                name: '',
                code: '',
                type_diagnostic: ''
            }
        }
    },
    methods: {
        onSubmit(event){
            event.preventDefault()
            const path= `${process.env.BASE_URI}diagnostic/${this.diagnosticId}/` 
        
            axios.put(path, this.form).then((response)=>{
                this.form.name = response.data.name
                this.form.code = response.data.code
                this.form.type_diagnostic = response.data.type_diagnostic
                swal("Diagnostico actualizado exitosamente.", "", "success")
           })
            .catch((error)=>{
                swal("No se ha podido actualizar el diagnostico.", "", "error")
            })
        },
        getDiagnostic(){
            const path= `${process.env.BASE_URI}diagnostic/${this.diagnosticId}/` 
        
            axios.get(path).then((response)=>{
                this.form.name = response.data.name
                this.form.code = response.data.code
                this.form.type_diagnostic = response.data.type_diagnostic
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        getTypeDiagnostic (){
            const path= `${process.env.BASE_URI}typeDiagnostic/` 
        
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
        this.getDiagnostic()
    }
}
</script> 