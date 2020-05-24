export default {
    namespaced: true,
    state: {
        phishTankDatabase: [],
        mitreEnterprise: [],
        mitreMobile: [],
        mitrePre: []
    },
    mutations: {
        setPhishTankDatabase(state, value) {
            state.phishTankDatabase = value;
        },
        setMitreEnterprise(state, value) {
            state.mitreEnterprise = value;
        },
        setMitreMobile(state, value) {
            state.mitreMobile = value;
        },
        setMitrePre(state, value) {
            state.mitrePre = value;
        }
    }
};
