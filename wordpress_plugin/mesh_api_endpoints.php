<?php
// Register custom REST endpoints for InfraFlow mesh status
add_action('rest_api_init', function () {
    register_rest_route('intraflow/v1', '/status', [
        'methods' => 'GET',
        'callback' => 'get_mesh_status'
    ]);

    register_rest_route('intraflow/v1', '/lastkey', [
        'methods' => 'GET',
        'callback' => 'get_last_qkd_key'
    ]);
});

function get_mesh_status() {
    return [
        'status' => '✅ Mesh Online',
        'timestamp' => current_time('mysql')
    ];
}

function get_last_qkd_key() {
    return get_option('intraflow_last_qkd_key', 'Not yet generated');
}
?>
