<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Registrar paciente {{form.name}}.</h2>              
            </div> 
        </div>       
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">  
                            <div class="form-group row">
                                <label for="id_type" class="col-sm-2 col-from-label">Tipo de identificación</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.id_type">
                                        <option >Cédula de ciudadania</option>
                                        <option >Tarjeta de identidad</option>
                                        <option >Número de pasaporte</option>
                                        <option >Cédula de extranjeria</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div>   
                            <div class="form-group row">
                                <label for="id_num" class="col-sm-2 col-from-label">Numero de identificación</label>
                                
                                <div class="col-sm-6">
                                    <b-form-input type="text" placeholder="Numero de identificación" name="id_num" class="form-control" v-model.trim="form.id_num"></b-form-input>  
                                </div>                                                                      
                            </div>                     
                            <div class="form-group row">
                                <label for="name" class="col-sm-2 col-from-label">Nombre</label>
                                
                                <div class="col-sm-6">
                                    <b-form-input :formatter="format" type="text" placeholder="Nombre" name="name" class="form-control" v-model.trim="form.name"></b-form-input> 
                                </div>                                                                      
                            </div>
                            <div class="form-group row">
                                <label for="lastname" class="col-sm-2 col-from-label">Apellido</label>
                                
                                <div class="col-sm-6">
                                    <b-form-input :formatter="format" type="text" placeholder="Apellido" name="lastname" class="form-control" v-model.trim="form.lastname"></b-form-input>                                  
                                </div>                                                                        
                            </div> 
                            <div class="form-group row">
                                <label for="genre" class="col-sm-2 col-from-label">Sexo</label>        
                                <div class="col-sm-6">
                                    <b-form-select class="mb-3" v-model.trim="form.genre">
                                        <option >Masculino</option>
                                        <option >Femenino</option>
                                    </b-form-select>                                      
                                </div>                                                                      
                            </div> 
                            <div class="form-group row">
                                <label for="occupation" class="col-sm-2 col-from-label">Ocupación</label>
                                
                                <div class="col-sm-6">
                                    <b-form-input :formatter="format" type="text" placeholder="Ocupación" name="occupation" class="form-control" v-model.trim="form.occupation"></b-form-input>                                  
                                </div>                                                                        
                            </div>
                            <div class="form-group row">
                                <label for="birthday" class="col-sm-2 col-from-label">Fecha de nacimiento</label>                             
                                <div class="col-sm-6">
                                    <b-form-input  type="date" name="birthday" class="form-control" v-model.trim="form.birthday"></b-form-input>                                  
                                </div>                                                                        
                            </div>   

                            <div class="form-group row">
                                <label for="entity" class="col-sm-2 col-from-label">Entidad medica</label>        
                                <div class="col-sm-6">

                                    <b-form-select entity class="mb-3" v-model.trim="form.entity">
                                    <template v-slot:first>
                                        <option :value="null" disabled>-- Porfavor selecione una entidad medica --</option>
                                    </template>
                                        <option v-for="entity in entity" :key="entity.id" :value="entity.id" >{{ entity.name }} </option>
                                    </b-form-select>
                                      
                                </div>                                                                      
                            </div>  
                            <div class="form-group row">
                                <label for="list_diagnostic" class="col-sm-2 col-from-label">Diagnostico</label>        
                                <div class="col-sm-6">

                                    <b-form-select diagnostic class="mb-3" v-model.trim="form.list_diagnostic">
                                    <template v-slot:first>
                                        <option :value="null" disabled>-- Porfavor selecione el diagnostico del paciente --</option>
                                    </template>
                                        <option v-for="diagnostic in diagnostic" :key="diagnostic.id" :value="diagnostic.id" >{{ diagnostic.name }} </option>
                                    </b-form-select>
                                      
                                </div>                                                                      
                            </div> 
                             <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="success">Crear</b-button>
                                    <b-button class="btn-large-space" :to="{ name: 'ListPatient' }">Cancelar</b-button>
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
            },
            entity: [],
            diagnostic: []
        }
    },
    methods: {
        onSubmit(event){
            event.preventDefault()
            const path= `${process.env.BASE_URI}patient/`
            axios.post(path, this.form).then((response)=>{
                this.form.id_type = response.data.id_type
                this.form.id_num = response.data.id_num
                this.form.name = response.data.name
                this.form.lastname = response.data.lastname
                this.form.genre = response.data.genre
                this.form.occupation = response.data.occupation
                this.form.birthday = response.data.birthday
                this.form.entity = response.data.entity
                this.form.list_diagnostic = response.data.list_diagnostic

                swal("Paciente creado exitosamente.", "", "success")
           })
            .catch((error)=>{
                swal("No se ha podido crear el paciente.", "", "error")
                console.log(error)
            })
        }, 
        getEntity (){
            const path= `${process.env.BASE_URI}entity/` 
        
            axios.get(path).then((response) =>{
                this.entity = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        getDiagnostic (){
            const path= `${process.env.BASE_URI}diagnostic/` 
        
            axios.get(path).then((response) =>{
                this.diagnostic = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        format(value, event) {
            return value.toLowerCase()
      }              
    },
    created(){
        this.getEntity()
        this.getDiagnostic ()
    }
}
</script>