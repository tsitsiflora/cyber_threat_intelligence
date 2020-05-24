<template>
    <div class="new-ioc-page">
        <h1 class="page-title">Add a new IoC</h1>

        <form @submit.prevent="addIoC">
            <div class="form-group">
                <label for="name">Name</label>
                <input id="name" name="name" placeholder="Enter name" type="text" class="form-control" required="required">
            </div>
            <div class="form-group">
                <label for="select">Type</label>
                <select id="select" name="select" class="form-control" required="required">
                    <option value="">Please select</option>
                    <option value="indicator">Indicator</option>
                    <option value="attack-pattern">Attack Pattern</option>
                    <option value="identity">Identity</option>
                    <option value="location">Location</option>
                    <option value="malware">Malware</option>
                    <option value="threat-actor">Threat actor</option>
                    <option value="tool">Tool</option>
                    <option value="vulnerability">Vulnerability</option>
                </select>
            </div>
            <div class="form-group">
                <label for="patternInput">Pattern</label>
                <textarea id="patternInput" name="patternInput" cols="40" rows="5" class="form-control" required="required"></textarea>
            </div>
            <div class="form-group">
                <label for="labels">Labels</label>
                <textarea id="labels" name="labels" cols="40" rows="5" class="form-control" aria-describedby="labelsHelpBlock"></textarea>
                <span id="labelsHelpBlock" class="form-text text-muted">Please enter the labels, comma separated</span>
            </div>
            <div class="form-group">
                <button name="submit" type="submit" class="btn btn-primary">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'NewIoC',
        components: {
        },
        data() {
            return {
            };
        },
        methods: {
            addIoC() {
                this.$swal({
                    title: "It's not working",
                    message: "You really thought this would work? Ha! Think again!",
                    icon: "warning"
                })
            }
        },
        computed: {
        }
    };
</script>

<style src="./NewIoC.scss" lang="scss" />
