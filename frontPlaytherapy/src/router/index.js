import Vue from 'vue'
import Router from 'vue-router'
import ListEntity from '@/components/Entity/ListEntity'
import UpdateEntity from '@/components/Entity/UpdateEntity'
import DeleteEntity from '@/components/Entity/DeleteEntity'
import CreateEntity from '@/components/Entity/CreateEntity'
import CreateTypeDiagnostic from '@/components/TypeDiagnostic/CreateTypeDiagnostic'
import UpdateTypeDiagnostic from '@/components/TypeDiagnostic/UpdateTypeDiagnostic'
import ListTypeDiagnostic from '@/components/TypeDiagnostic/ListTypeDiagnostic'
import DeleteTypeDiagnostic from '@/components/TypeDiagnostic/DeleteTypeDiagnostic'
import CreateDiagnostic from '@/components/Diagnostic/CreateDiagnostic'
import ListDiagnostic from '@/components/Diagnostic/ListDiagnostic'
import UpdateDiagnostic from '@/components/Diagnostic/UpdateDiagnostic'
import CreatePatient from '@/components/Patient/CreatePatient'
import ListPatient from '@/components/Patient/ListPatient'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/entitys',
      name: 'ListEntity',
      component: ListEntity
    },
    {
      path: '/entitys/:entityId/update',
      name: 'UpdateEntity',
      component: UpdateEntity
    },
    {
      path: '/entitys/:entityId/delete',
      name: 'DeleteEntity',
      component: DeleteEntity
    },
    {
      path: '/entitys/create',
      name: 'CreateEntity',
      component: CreateEntity
    },
    {
      path: '/typeDiagnostic/create',
      name: 'CreateTypeDiagnostic',
      component: CreateTypeDiagnostic
    },
    {
      path: '/typeDiagnostic/:typeDiagnosticId/update',
      name: 'UpdateTypeDiagnostic',
      component: UpdateTypeDiagnostic
    },
    {
      path: '/typeDiagnostic',
      name: 'ListTypeDiagnostic',
      component: ListTypeDiagnostic
    },
    {
      path: '/typeDiagnostic/:typeDiagnosticId/delete',
      name: 'DeleteTypeDiagnostic',
      component: DeleteTypeDiagnostic
    },
    {
      path: '/diagnostic/create',
      name: 'CreateDiagnostic',
      component: CreateDiagnostic
    },
    {
      path: '/diagnostic',
      name: 'ListDiagnostic',
      component: ListDiagnostic
    },
    {
      path: '/diagnostic/:diagnosticId/update',
      name: 'UpdateDiagnostic',
      component: UpdateDiagnostic
    },
    {
      path: '/patient/create',
      name: 'CreatePatient',
      component: CreatePatient
    }
    ,
    {
      path: '/patient',
      name: 'ListPatient',
      component: ListPatient
    }
  ],
  mode: 'history'
})
